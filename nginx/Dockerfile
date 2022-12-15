# Runs from the nginx image
FROM nginx

# Deletes already put in place conf file
# RUN rm /etc/nginx/conf.d/default.conf

# Copies literal nginx.conf file to ngix conf.d directory to set the configuration
COPY nginx.conf /etc/nginx/conf.d
