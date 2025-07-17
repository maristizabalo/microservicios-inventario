from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class GatewayAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        
        user_id = validated_token.get("user_id")
        if not user_id:
            raise AuthenticationFailed("Invalid token: no user_id")
        
        return type('User', (), {'id': user_id, 'is_authenticated': True})()
