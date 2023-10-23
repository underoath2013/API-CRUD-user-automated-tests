user_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {
            "type": "string"
        },
        "status": {
            "type": "string"
        },
        "message": {
            "type": "string"
        },
        "result": {
            "type": ["array", "object"],
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "age": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },
                        "id": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "age",
                        "name",
                        "id"
                    ]
                }
            ]
        }
    },
    "required": [
        "code",
        "status",
        "message"
    ]
}
