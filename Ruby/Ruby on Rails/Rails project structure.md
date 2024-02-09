- **app** − It organizes your application components. It's got subdirectories that hold the view (views and helpers), controller (controllers), and the backend business logic (models).

- **app/controllers** − The controllers subdirectory is where Rails looks to find the controller classes. A controller handles a web request from the user.

- **app/helpers** − The helpers subdirectory holds any helper classes used to assist the model, view, and controller classes. This helps to keep the model, view, and controller code small, focused, and uncluttered.

- **app/models** − The models subdirectory holds the classes that model and wrap the data stored in our application's database. In most frameworks, this part of the application can grow pretty messy, tedious, verbose, and error-prone. Rails makes it dead simple!

- **app/view** − The views subdirectory holds the display templates to fill in with data from our application, convert to HTML, and return to the user's browser.

- **app/view/layouts** − Holds the template files for layouts to be used with views. This models the common header/footer method of wrapping views. In your views, define a layout using the <tt>layout:default</tt> and create a file named default.html.erb. Inside default.html.erb, call <% yield %> to render the view using this layout.

- **components** − This directory holds components, tiny self-contained applications that bundle model, view, and controller.

- **config** − This directory contains the small amount of configuration code that your application will need, including your database configuration (in database.yml), your Rails environment structure (environment.rb), and routing of incoming web requests (routes.rb). You can also tailor the behavior of the three Rails environments for test, development, and deployment with files found in the environments directory.

- **db** − Usually, your Rails application will have model objects that access relational database tables. You can manage the relational database with scripts you create and place in this directory.

- **doc** − Ruby has a framework, called RubyDoc, that can automatically generate documentation for code you create. You can assist RubyDoc with comments in your code. This directory holds all the RubyDoc-generated Rails and application documentation.

- **lib** − You'll put libraries here, unless they explicitly belong elsewhere (such as vendor libraries).

- **log** − Error logs go here. Rails creates scripts that help you manage various error logs. You'll find separate logs for the server (server.log) and each Rails environment (development.log, test.log, and production.log).

- **public** − Like the public directory for a web server, this directory has web files that don't change, such as JavaScript files (public/javascripts), graphics (public/images), stylesheets (public/stylesheets), and HTML files (public).

- **script** − This directory holds scripts to launch and manage the various tools that you'll use with Rails. For example, there are scripts to generate code (generate) and launch the web server (server).

- **test** − The tests you write and those that Rails creates for you, all goes here. You'll see a subdirectory for mocks (mocks), unit tests (unit), fixtures (fixtures), and functional tests (functional).

- **tmp** − Rails uses this directory to hold temporary files for intermediate processing.

- **vendor** − Libraries provided by third-party vendors (such as security libraries or database utilities beyond the basic Rails distribution) go here.