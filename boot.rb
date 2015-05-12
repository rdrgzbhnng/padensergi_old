require 'bundler/setup'
require 'sinatra'
Bundler.require(:default, Sinatra::Base.environment)

enable :sessions

configure :production do
  require 'rack/protection'
  use Rack::Protection
  use Rack::Deflater
  set :session_secret, ENV['SESSION_SECRET']
end
