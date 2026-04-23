# API Reference

This page demonstrates how to document an API in Markdown — a common use case for Docs as Code.

!!! info "This is a demo"
    The endpoints below are illustrative examples showing how technical API docs look when written as Markdown and rendered by MkDocs.

---

## Base URL

```
https://api.example.com/v2
```

All requests must include an `Authorization` header:

```http
Authorization: Bearer <your-token>
```

---

## Endpoints

### `GET /users`

Returns a paginated list of users.

**Query Parameters**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number (default: `1`) |
| `per_page` | integer | No | Results per page (default: `20`, max: `100`) |
| `search` | string | No | Filter by name or email |

**Example Request**

```bash
curl -X GET "https://api.example.com/v2/users?page=1&per_page=10" \
  -H "Authorization: Bearer eyJhbGci..."
```

**Example Response**

```json
{
  "data": [
    {
      "id": "usr_01HX2K",
      "name": "Ada Lovelace",
      "email": "ada@example.com",
      "created_at": "2024-01-15T09:00:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 42
  }
}
```

---

### `POST /users`

Creates a new user.

**Request Body**

```json
{
  "name": "Grace Hopper",
  "email": "grace@example.com",
  "role": "admin"
}
```

**Response Codes**

| Code | Meaning |
|---|---|
| `201 Created` | User created successfully |
| `400 Bad Request` | Missing or invalid fields |
| `409 Conflict` | Email already exists |

---

### `DELETE /users/{id}`

!!! warning "Irreversible"
    This action permanently deletes the user and all associated data. It cannot be undone.

**Path Parameters**

| Parameter | Type | Description |
|---|---|---|
| `id` | string | The user ID (e.g., `usr_01HX2K`) |

**Example Request**

```bash
curl -X DELETE "https://api.example.com/v2/users/usr_01HX2K" \
  -H "Authorization: Bearer eyJhbGci..."
```

---

## Error Format

All errors follow a consistent structure:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The 'email' field is required.",
    "field": "email"
  }
}
```

**[← Configuration](getting-started/configuration.md)** | **[Changelog →](changelog.md)**
