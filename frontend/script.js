// Kod wykonuje się w przeglądarce użytkownika, a nie w kontenerze frontendu,
// dlatego backend jest pod adresem widocznym z hosta (port wystawiony przez -p 5000:5000)
const API_URL = "http://localhost:5000/check";

// SHA-1 liczony w przeglądarce - hasło w postaci jawnej nie opuszcza komputera
async function sha1(text) {
  const bytes = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest("SHA-1", bytes);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

document.getElementById("check-form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const result = document.getElementById("result");
  const password = document.getElementById("password").value;

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ hash: await sha1(password) }),
    });
    const data = await response.json();
    result.textContent = data.found
      ? "To hasło występuje w próbce wycieków - nie używaj go."
      : "Tego hasła nie ma w próbce wycieków (co nie znaczy, że jest bezpieczne).";
  } catch (err) {
    result.textContent = "Brak połączenia z backendem.";
  }
});
