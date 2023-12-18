# GitHub Actions CI/CD Project

This project aims to create a Continuous Integration (CI) procedure for a simple web application using Flask. It was created for educational purposes to help me become familiar with GitHub Actions, a CI/CD platform.

## Technologies Used

- **Python**
- **Flask**
- **Docker**
- **Docker Hub**
- **GitHub Actions**
- **Git**

## Project Details

This project consists of a Flask web application that returns a simple message to the user when visiting the server's endpoint (Home Page). When the developer makes changes to the code and pushes a new version of the application to the GitHub repo, the following actions take place:

- **Testing**
  1. Code is ** checked out ** to be available from GitHub servers.
  2. Python is set up, and the necessary dependencies are installed along with the required libraries.
  3. Tests are run based on the **pytest** library.

- **Building**
  1. Building is conducted only if the testing job is ** finished successfully **.
  2. Code is checked out.
  3. Docker buildx and QEMU is set up.
  4. Login credentials are passed using **GitHub Secrets**.
  5. Docker image is built and sent to the Docker Hub repo that is specified.

- **Deployment**
  1. The image is delivered to Docker Hub, and we can deploy it whenever needed.
  2. Use the `docker pull` command to retrieve the updated image.
  3. Run the application live on localhost.

## Future Extensions

For future development, an extension may involve creating a more advanced web application that should pass sophisticated tests before undergoing the build and deployment processes. By leveraging buildx, a tool capable of constructing images for multiple platforms, and qemu, a platform emulator, we can build and deploy images compatible with various operating systems and architectures in a future extension.

Additionally, the adoption of a Continuous Deployment approach, as opposed to Continuous Delivery, would enhance my knowledge-building efforts.

