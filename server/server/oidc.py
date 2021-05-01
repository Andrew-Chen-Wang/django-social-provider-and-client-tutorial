from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    def get_additional_claims(self, request):
        """
        JWT Claims are NOT encrypted. They aren't encrypted (I have to repeat
        myself because according to SAT statistics, even with bolded, upper-cased
        letters, many students still miss it.
        """
        # The default for sub is request.user.id, but the clients most likely
        # don't need an ID from your server. That's just my opinion security-wise.
        return {
            "sub": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }

    def get_userinfo_claims(self, request):
        """
        This just calls self.get_additional_claims, but both are not encrypted!
        This is different in that this is for the /o/userinfo/ endpoint, whereas
        the other is just to get claims during regular authorization flow.

        Example Usage:
        claims = super().get_userinfo_claims(request)
        claims["color_scheme"] = get_color_scheme(request.user)
        return claims
        """
        return super(CustomOAuth2Validator, self).get_userinfo_claims(request)

    def validate_silent_login(self, request):
        pass

    def introspect_token(self, token, token_type_hint, request, *args, **kwargs):
        pass

    def validate_silent_authorization(self, request):
        pass
