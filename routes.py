from controllers import LoginUserControllers, LoginUserControllers2 , LoginUserControllers3, LoginUserControllers4

user = {
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "login2_user": "/api/v01/user/login2", "login2_user_controllers": LoginUserControllers2.as_view("login2_api"),
    "login3_user": "/api/v01/user/login3", "login3_user_controllers": LoginUserControllers3.as_view("login3_api"),
    "login4_user": "/api/v01/user/login4", "login4_user_controllers": LoginUserControllers4.as_view("login4_api"),

}

