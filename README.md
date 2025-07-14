# Face Verification with FHE

[Literature Review](https://docs.google.com/spreadsheets/d/1mCAT-ed-GVVxZa37B59JbQOE4M8YQZJGOw7yOSyBrYA/edit?gid=0#gid=0)

## General Pipeline

**Enrollment phase:**
- Face image → Face embedding (via FaceNet or ArcFace)
- Encrypt embedding with FHE → Store on server

**Verification phase:**
- New face image → Embedding (locally)
- Encrypt embedding → Send to server
- Server performs encrypted similarity computation (Euclidean distance or cosine similarity)
- Server sends encrypted result → Decrypted locally → Accept/Reject
