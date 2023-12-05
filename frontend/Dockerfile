FROM node:21 as BUILD

WORKDIR /app

COPY ./package.json ./
COPY ./package-lock.json ./
RUN npm i

COPY ./ ./
RUN npm run build

# ---

FROM nginx:1.23-alpine

COPY --from=BUILD /app/build /usr/share/nginx/html
