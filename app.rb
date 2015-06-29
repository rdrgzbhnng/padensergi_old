require './boot.rb'

get '/' do
  erb :verkami
end

get '/castellano' do
  erb :verkami
end

get '/verkami' do
  erb :verkami
end

get '/anterior' do
  erb :catala
end
