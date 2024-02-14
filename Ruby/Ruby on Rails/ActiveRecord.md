ActiveRecord is the M in [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) - the model - which is the layer of the system responsible for representing business data and logic. Active Record facilitates the creation and use of business objects whose data requires persistent storage to a database. It is an implementation of the Active Record pattern which itself is a description of an Object Relational Mapping system.

## Naming Convention

By default, Active Record uses some naming conventions to find out how the mapping between models and database tables should be created. Rails will pluralize your class names to find the respective database table. So, for a class `Book`, you should have a database table called **books**. The Rails pluralization mechanisms are very powerful, being capable of pluralizing (and singularizing) both regular and irregular words. When using class names composed of two or more words, the model class name should follow the Ruby conventions, using the CamelCase form, while the table name must use the snake_case form. Examples:

- Model Class - Singular with the first letter of each word capitalized (e.g., `BookClub`).
- Database Table - Plural with underscores separating words (e.g., `book_clubs`).


## How to identify N+1 queries in a Rails app? 🕵🏻‍♂️

There are several ways you can detect N+1 queries in a Rails application:

1. Using a tool like the [bullet gem](https://github.com/flyerhzm/bullet) (or Rails built-in strict loading mode), which can automatically detect and alert you of N+1 queries.
2. Using `NewRelic` to monitor the performance of your application and, while on it, identify N+1 queries.
3. Similarly to New Relic, you can locally use both the [rack-mini-profiler](https://github.com/MiniProfiler/rack-mini-profiler) and the [stackprof](https://github.com/tmm1/stackprof) gems to plot flame graphs and, thus, detect N+1s.
4. Manually review your application’s log files and look for repeated queries that are being executed.

Keep in mind that it’s not always possible to completely eliminate N+1 queries from a Rails application. Still, by using these tools and techniques you should be able to identify the N+1 queries causing performance issues.

# How to prevent N+1 queries on Rails? ‍👨🏻‍⚕️

Here are some strategies you can use to prevent N+1 queries in a Rails application:

## Use the `bullet` gem (old but gold)

The `bullet` gem can automatically detect and alert you to N+1 queries in your application. It also suggests ways to optimize the queries, such as by using the already mentioned `includes`. However, if you're using a more recent version of Rails, the next option might work best for you.

## Use strict_loading (preferred)

Strict loading was introduced in Rails 6.1. Prior to Rails 6.1, there was no built-in way to enable strict loading in a Rails application. You would have to manually check if the association had been loaded before accessing it, or use a tool like the `bullet` gem to detect N+1 queries.

By default, Rails will not raise an error if you try to access an association that has not been loaded. However, you can manually use the `strict_loading` option to cause an error to be raised if you try to access an unloaded association. This can help prevent N+1 queries by alerting you about cases where you accidentally executed unnecessary queries.

To use strict loading in a Rails application, you can set the `strict_loading` option to `true` for the association you want to enable strict loading for.

For example, suppose you have a `Post` model that has many `Comment` models, and you want to enable strict loading for the `comments` association. You can set the `strict_loading` option as follows:
```ruby
# Enable strict loading for the comments association on the Post model  
class Post < ApplicationRecord  
  has_many :comments, strict_loading: true  
end  
  
  
# This will raise a StrictLoadingError exception, because the comments have not been loaded  
Post.first.comments.each do |comment|  
  puts comment.body  
end
```

If you don't want to activate strict loading mode for all queries coming from this association, you can also do it on a per-query basis:

```ruby
post = Post.strict_loading.first  
  
# This will raise an ActiveRecord::StrictLoadingViolationError  
post.comments.to_a
```

You could also choose to activate strict loading for the whole app, or only on logs, it's really up to you.


SOURCES:
n+1: https://medium.com/doctolib/how-to-find-fix-and-prevent-n-1-queries-on-rails-6b30d9cfbbaf