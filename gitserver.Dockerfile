FROM node:alpine
RUN apk add --no-cache tini git \
    && yarn global add git-http-server \
    && adduser -D -g git git
USER git
WORKDIR /home/git
RUN git init --bare repository.git
RUN git config --global user.name "Tee Hong Huat" \
    && git config --global user.email "2301911@SIT.singaporetech.edu.sg"
ENTRYPOINT ["tini", "--", "git-http-server", "-p", "3000", "/home/git"]
