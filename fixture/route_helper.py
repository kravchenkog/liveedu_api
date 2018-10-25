
class Route:
    def __init__(self):
        self.check_email = '/api/v3/auth/registration/check-email/'
        self.get_public_key = '/api/v3/auth/public-key/'
        self.check_password = '/api/v3/auth/registration/check-password/'
        self.check_username = '/api/v3/auth/registration/check-username/'
        self.register = '/api/v3/auth/registration/register/'
        self.topics = '/api/v3/topics/'
        self.email_confirmation = '/api/v3/auth/registration/verify-email/'
        self.login = '/api/v3/auth/login/'
        self.me = '/api/v3/me/'
        self.me_balanses = "/api/v3/me/balances/"
        self.me_balanses_s = "/api/v3/me/balances/subscription"
        self.me_balanses_c = "/api/v3/me/balances/creator"
        self.me_billing_history = "/api/v3/me/billing/history/"
        self.me_chat_cred = "/api/v3/me/chat/credentials/"
        self.me_followers = "/api/v3/me/followers/"
        self.me_following = "/api/v3/me/following/"
        self.me_preferences = "/api/v3/me/notification/preferences/"
        self.me_subscr_notif = "/api/v3/me/notification/subscriptions/"
        self.me_payment_methods = "/api/v3/me/payment-methods/"
        self.categories = '/api/v3/categories/'
        self.languages = '/api/v3/languages/'
        self.languages_iso = '/api/v3/languages/'
        self.topic_hierarchy = '/api/v3/topics-hierarchy/'
        self.projects = '/api/v3/projects/' #GET/POST
        self.subscription = '/api/v3/me/subscription/'
        self.plans = '/api/v3/plans/'
        self.transaction_ledu = "/api/v3/me/balances/subscription/transactions/"











