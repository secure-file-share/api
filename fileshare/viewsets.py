from django.http import FileResponse
from alpha.viewsets import BaseAuthViewSet
from alpha.utilities import parse_request_body
from client.models import User
from .models import Files, FileShare
from .serializers import FileShareSerializer  # , FileSerializer
from .crypto import decrypt_file
from .utilities import is_valid_uuid
from .exceptions import EncryptionKeyMismatch


class FileShareViewSet(BaseAuthViewSet):
    """
    File Share API
    """

    def list(self, request):
        try:
            # GET USER WHO REQUESTS
            user = request.user

            # GET CURRENT USER'S ALL FILES
            file_share_with_you = FileShare.objects.filter(shared_to=user)
            file_share_by_you = FileShare.objects.filter(created_by=user)

            # SERIALIZED FILES
            files_serialized = {
                "shared_with_you": FileShareSerializer(file_share_with_you, many=True).data,
                "shared_by_you": FileShareSerializer(file_share_by_you, many=True).data
            }
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'fileshare.viewsets.FileShareViewSet.list'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=files_serialized)

    def retrieve(self, request, pk):
        try:
            # USE EITHER UNIQUE CODE OR PRIMARY KEY
            if is_valid_uuid(pk):
                file_share = FileShare.objects.get(pk=pk)
            else:
                file_share = FileShare.objects.get(unique_code=pk)

            # CHECK PERMISSION
            if request.user not in (file_share.shared_to, file_share.shared_by):
                # ONLY ACCESS IF THIS FILE IS SHARED TO THE USER WHO REQUESTS
                return self.error_response(message="You have no access to this file!", status=self.status.HTTP_401_UNAUTHORIZED)

            # GET KEY TO DECRYPT FILE
            key = file_share.organization.secret_key

            # DECRYPT FILE
            decrypted_file = decrypt_file(key, file_share.file)

            if decrypted_file == 0:
                # KEY MISMATCH EXCEPTION
                raise EncryptionKeyMismatch
        except FileShare.DoesNotExist:
            return self.error_response(message="The file does not exist!", status=self.status.HTTP_404_NOT_FOUND)
        except EncryptionKeyMismatch as e:
            return self.error_response(message=str(e))
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'fileshare.viewsets.FileShareViewSet.retrieve'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return FileResponse(open(decrypted_file, "rb"))

    def create(self, request):
        try:
            # PARSE REQUEST BODY
            data = parse_request_body(request)

            # GET FILE
            file_instance = data.get("file")

            if not file_instance:
                return self.error_response(message="'file' is required!", status=self.status.HTTP_400_BAD_REQUEST)

            # GET USER TO SHARE
            shared_to = data.get("shared_to")
            if not shared_to:
                return self.error_response(message="'shared_to' is required!", status=self.status.HTTP_400_BAD_REQUEST)

            shared_to = User.objects.get(username=shared_to)

            if shared_to.organization != request.user.organization:
                # USER CANNOT SHARE FILES TO USERS OF OTHER ORGANIZATION
                return self.error_response(message="You cannot share this file with this user", status=self.status.HTTP_403_FORBIDDEN)

            # CREATE FILE INSTANCE
            file_obj = Files()
            file_obj.file_instance = file_instance
            file_obj.organization = shared_to.organization
            file_obj.save()

            file_share = FileShare.objects.create(
                file_instance=file_obj,
                shared_to=shared_to
            )

            # FILE SERIALIZED
            file_serialized = FileShareSerializer(file_share).data
        except User.DoesNotExist:
            return self.error_response(message="User does not exist", status=self.status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'fileshare.viewsets.FileShareViewSet.create'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=file_serialized, message="File uploaded!", status=self.status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        try:
            file_share = FileShare.objects.get(pk=pk)

            if file_share.organization != request.user.organization:
                # USER CANNOT ACCESS OTHER ORGANIZATION FILES
                return self.error_response(message="You have no access to this file!", status=self.status.HTTP_401_UNAUTHORIZED)

            if file_share.created_by != request.user:
                # USER CANNOT DELETE OTHER'S FILES
                return self.error_response(message="You cannot delete this file!", status=self.status.HTTP_401_UNAUTHORIZED)

            # DELETE FILE
            file_serialized = FileShareSerializer(file_share).data
            file_share.delete()
        except FileShare.DoesNotExist:
            return self.error_response(message="The file does not exist!", status=self.status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'fileshare.viewsets.FileShareViewSet.destroy'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=file_serialized, message="File deleted!")
