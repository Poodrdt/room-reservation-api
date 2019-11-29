1. Not PEP8 compliant
2. Every table should hold information about when it was `created_at` and `updated_at`

4. Tests should not only test the status of a response, but also what data was retrieved/created/updated
5. In every TestCase setup method you're creating a user. This could have been implemented via a base TestCase class, which would be inherited by every TestCase

7. logging is configured, but not used anywhere

9. No api docs
