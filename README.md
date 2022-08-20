# special-potato

---

## Send Message

---

```bash
curl --location --request POST 'https://special-potato.tendean.my.id/core/' \
--form 'room_name="alpha"' \
--form 'user_name="tendean"' \
--form 'user_message="yohohoho"'
```

```json
{
  "status_code": 200,
  "message": "Success.",
  "data": {}
}
```

---

```bash
curl --location --request POST 'https://special-potato.tendean.my.id/core/' \
--form 'room_name="alpha"' \
--form 'user_name="arter"' \
--form 'user_message="hello world :)"'
```

```json
{
  "status_code": 200,
  "message": "Success.",
  "data": {}
}
```

---

## Get Message from Room

```bash
curl --location --request GET 'http://special-potato.tendean.my.id/core/?room_name=alpha' \
--form 'room_name="testing"' \
--form 'user_name="arter"' \
--form 'user_message="test"'
```

```json
{
  "status_code": 200,
  "message": "Success.",
  "data": {
    "room_name": "alpha",
    "chats": [
      {
        "user": "tendean",
        "message": "yohohoho",
        "created_at": 1661020977.637774
      },
      {
        "user": "arter",
        "message": "hello world :)",
        "created_at": 1661020941.288635
      }
    ]
  }
}
```

## Screenshots (Postman)

- https://cdn.discordapp.com/attachments/858938620425404426/1010621261799489686/unknown.png
- https://cdn.discordapp.com/attachments/858938620425404426/1010621295278428170/unknown.png
- https://cdn.discordapp.com/attachments/858938620425404426/1010621323187327067/unknown.png
