error_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "detail": {
            "type": ["array", "string"],
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "loc": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "msg": {
                            "type": "string"
                        },
                        "type": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "loc",
                        "msg",
                        "type"
                    ]
                }
            ]
        }
    },
    "required": [
        "detail"
    ]
}
