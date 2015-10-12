class User < ActiveRecord::Base
  attr_accessible :username, :hashed_password, :salt, :profile, :bitbars

  validates :username, format: { with: /^[a-zA-Z0-9_]*$/,
      message: "must be letters, numbers, or underscore", :multiline => true }
end
