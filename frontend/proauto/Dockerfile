FROM node:18.16.0

WORKDIR /proauto

COPY package*.json ./

RUN npm install

RUN npm audit fix

COPY . .

EXPOSE 5173