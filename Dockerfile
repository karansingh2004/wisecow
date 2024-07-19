FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt install fortune-mod cowsay -y

# Copy the wisecow.sh file
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Expose the port
EXPOSE 4499

# Run the script when the container starts
CMD ["/app/wisecow.sh"]
