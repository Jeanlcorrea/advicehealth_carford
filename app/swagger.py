from flask import jsonify

def swagger():
    swag = {
        "swagger": "2.0",
        "info": {
            "title": "Car Management API",
            "version": "1.0.0",
            "description": "API for managing cars and car owners"
        },
        "tags": [
            {
                "name": "owners",
                "description": "Operations related to car owners"
            },
            {
                "name": "cars",
                "description": "Operations related to cars"
            }
        ],
        "paths": {
            "/cars": {
                "post": {
                    "tags": ["cars"],
                    "summary": "Add a new car",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "color": {
                                        "type": "string",
                                        "enum": ["yellow", "blue", "gray"]
                                    },
                                    "model": {
                                        "type": "string",
                                        "enum": ["hatch", "sedan", "convertible"]
                                    },
                                    "owner_id": {
                                        "type": "integer"
                                    }
                                }
                            }
                        }
                    ],
                    "responses": {
                        "201": {
                            "description": "Car added successfully",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Car added successfully"
                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "Bad request",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "Owner does not exist",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/cars/{car_id}": {
                "delete": {
                    "tags": ["cars"],
                    "summary": "Delete a car",
                    "parameters": [
                        {
                            "name": "car_id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Car deleted successfully",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Car deleted successfully"
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "Car not found",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Car not found"
                                    }
                                }
                            }
                        },
                        "500": {
                            "description": "Internal server error",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/car_owners": {
                "post": {
                    "tags": ["owners"],
                    "summary": "Add a new car owner",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "email": {
                                        "type": "string",
                                        "format": "email"
                                    }
                                }
                            }
                        }
                    ],
                    "responses": {
                        "201": {
                            "description": "Car owner added successfully",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Car owner added successfully"
                                    },
                                    "owner_id": {
                                        "type": "integer"
                                    }
                                }
                            }
                        },
                        "500": {
                            "description": "Internal server error",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                },
                "get": {
                    "tags": ["owners"],
                    "summary": "Get all car owners",
                    "responses": {
                        "200": {
                            "description": "Successful response with a list of car owners",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "email": {
                                            "type": "string",
                                            "format": "email"
                                        }
                                    }
                                }
                            }
                        },
                        "500": {
                            "description": "Internal server error",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/car_owners/{owner_id}/cars": {
                "get": {
                    "tags": ["owners"],
                    "summary": "Get cars owned by a specific owner",
                    "parameters": [
                        {
                            "name": "owner_id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response with a list of cars owned by the owner",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "color": {
                                            "type": "string"
                                        },
                                        "model": {
                                            "type": "string"
                                        },
                                        "owner_id": {
                                            "type": "integer"
                                        }
                                    }
                                }
                            }
                        },
                        "400": {
                            "description": "Bad request",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/car_owners/{owner_id}": {
                "delete": {
                    "tags": ["owners"],
                    "summary": "Delete a car owner and their associated cars",
                    "parameters": [
                        {
                            "name": "owner_id",
                            "in": "path",
                            "required": True,
                            "type": "integer"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Car owner and associated cars deleted successfully",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Car owner and associated cars deleted successfully"
                                    }
                                }
                            }
                        },
                        "404": {
                            "description": "Owner not found",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string",
                                        "example": "Owner not found"
                                    }
                                }
                            }
                        },
                        "500": {
                            "description": "Internal server error",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "message": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return jsonify(swag)
