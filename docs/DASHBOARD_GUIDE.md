# Monitoring Dashboard Hosting Guide

To monitor your automations, you need a REST API and a dashboard. Here are the best ways to host this for free.

## Option 1: Supabase (Recommended)
**Supabase** is a free, open-source Firebase alternative.
- **Database**: Free PostgreSQL database.
- **REST API**: Automatically generated based on your table schema.
- **Auth**: Built-in authentication.
- **Setup**:
  1. Create a project at [supabase.com](https://supabase.com/).
  2. Create an `execution_logs` table using the schema in `docs/schema.sql`.
  3. In n8n, use the **HTTP Request** node to POST data to the Supabase API endpoint.

## Option 2: Render or Railway
Use these platforms to host a custom **FastAPI** or **Node.js** dashboard.
- **Render**: Offers a free tier for web services.
- **Railway**: Offers a "Trial" plan with free credits.
- **Setup**:
  1. Push your dashboard code to GitHub.
  2. Connect your GitHub repo to Render/Railway.
  3. They will automatically deploy and give you a public URL.

## Option 3: n8n Internal Dashboard
Did you know n8n can also serve as a dashboard?
- Use a **Webhook** node as a trigger.
- Use a **Code** node to fetch logs from the DB.
- Use a **Response** node to return a beautiful HTML table with CSS.
- This way, your dashboard lives inside your automation system!

## Option 4: Free Static Hosting (Frontend Only)
If your API is already hosted (e.g., Supabase), you can host the UI on:
- **Vercel**
- **Netlify**
- **GitHub Pages**

### Suggested Payload for Dashboard API:
```json
{
  "task_id": "TASK_001",
  "name": "System Check",
  "status": "SUCCESS",
  "duration": 2.45,
  "timestamp": "2024-05-15T10:30:00Z",
  "logs": "Starting... Done."
}
```
