# SecureFileShare

CPSC-69100
<br />
Computer Science Masters Project
<br />
Fall 2023
<br />
Lewis University

<strong>Work By,</strong>
<br />
Dristi Pande (L30065598)
<br />
Aashirwad Shrestha (L30063660)
<br />
Satshree Shrestha (L30063661)

# About

The SecureFileShare project aims to develop a simple yet robust web application that allows organizations to securely transfer and share files among their members. In today's digital age, sharing sensitive documents and data securely is of utmost importance. Our web app will provide a user-friendly platform for organizations to sign up, upload files, set access permissions, and share files securely with team members or external collaborators. The application will employ industry-standard encryption and authentication techniques to ensure data confidentiality and integrity.

# Automated Bash Scripts

<strong>Run these bash scripts from `development` branch only!</strong>

- git_merge_push.sh
  > Merge and push commited changes of `development` branch to `main` branch.
- git_merge.sh
  > Only merge commited changes of `development` branch to `main` branch.

# Cloudinary

To use Cloudinary storage for media uploads, set `USE_CLOUDINARY` as `true`.

These <b>Cloudinary</b> attributes are <b>required</b> and initialized as empty string by default. These can be initialized in local settings as well.

- CLOUDINARY_API_KEY
- CLOUDINARY_API_SECRET
- CLOUDINARY_CLOUD_NAME
