FROM redis:6.2.6
RUN mkdir ./projectFiles
COPY . ./projectFiles
EXPOSE 6379
RUN redis-server
CMD ["python", "manage.py", "runserver"]


