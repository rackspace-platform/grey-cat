import web

urls = (
  '/', 'index',
)


class index:
    def GET(self):
        return "Hello, world in grey-cat application!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
