FROM node:12.14 as build

WORKDIR /usr/src/app

ENV PATH $PATH:/usr/src/app/node_modules/.bin

COPY package*.json ./
RUN npm ci

COPY . .

ENV REACT_APP_GATEWAY_API_HOST $REACT_APP_GATEWAY_API_HOST
#ENV REACT_APP_GATEWAY_API_PORT $REACT_APP_GATEWAY_API_PORT

RUN npm run build

# production environment
FROM nginx:stable-alpine
COPY --from=build /usr/src/app/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]