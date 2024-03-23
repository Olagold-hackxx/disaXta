FROM node:18.17.1-alpine
ENV NODE_ENV=production
ENV npm_config_cache=/oauth

WORKDIR /oauth
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --production --silent && mv node_modules ../
COPY . .
EXPOSE 3000
RUN chmod -R a+rwx /oauth
CMD ["npm", "start"]
