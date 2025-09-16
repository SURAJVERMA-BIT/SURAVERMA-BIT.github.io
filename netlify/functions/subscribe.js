import { neon } from "@netlify/neon";

export async function handler(event, context) {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: "Method Not Allowed" })
    };
  }

  try {
    const sql = neon(); // DB connection
    const body = JSON.parse(event.body);
    const email = body.email;

    if (!email) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: "Email is required" })
      };
    }

    // Create table if not exists
    await sql`
      CREATE TABLE IF NOT EXISTS waiting_list (
        id SERIAL PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
      )
    `;

    // Insert email
    await sql`INSERT INTO waiting_list (email) VALUES (${email})`;

    return {
      statusCode: 200,
      body: JSON.stringify({ message: "You’re on the waitlist! 🎉" })
    };
  } catch (error) {
    if (error.message.includes("duplicate key")) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: "This email is already registered!" })
      };
    }
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Server error, please try later." })
    };
  }
}
