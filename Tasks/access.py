from rest_access_policy import AccessPolicy


class TaskPolicy(AccessPolicy):
    statements = [
        {
            "action": ["partial_update", "update"],
            "principal": "*",
            "effect": "deny",
            "condition": ["is_menger"],
        },
        {
            "action": ["*"],
            "principal": ["*"],
            "effect": "allow",
        },
    ]

    def is_menger(self, request, view, action) -> bool:
        return not view.get_object().bucket.menger == request.user

