FROM node:21 AS builder

WORKDIR /app

COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm install --include=dev

COPY ./ ./

FROM node:21 AS build

WORKDIR /app

COPY --from=builder /app/ ./

RUN npm run build

# ---

FROM nginx:1.23-alpine

COPY --from=build /app/build /usr/share/nginx/html
