FROM python:3.10-slim-bullseye


# Set the working directory
WORKDIR /bot_report

# Copy files from your host to your current working directory
COPY . .
# Build the application with cmake

RUN chmod a+x /bot_report/bot.py
RUN pip install -r requirements.txt


CMD ["/bot_report/bot.py"]
ENTRYPOINT ["python3"]
