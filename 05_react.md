# React / Frontend Interview Questions

Importance: ⭐⭐⭐ = Asked 3+ times | ⭐⭐ = Asked 2 times | ⭐ = Asked once

Note: These came up likely because of frontend exposure in your projects.
Not a deep focus area but worth knowing the basics.

---

## React

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What are React Hooks | 1x (Q11) | ⭐ |
| What are session and cookies in React JS | 1x (Q140) | ⭐ |
| Can we transfer session data from one session to another | 1x (Q141) | ⭐ |

---

## Angular

| Question | Times Asked | Importance |
|----------|-------------|------------|
| What is Angular lifecycle | 1x (Q12) | ⭐ |

---

## General Frontend

| Question | Times Asked | Importance |
|----------|-------------|------------|
| Do you know JavaScript | 1x (Q150) | ⭐ |

---
---
---
# React / Frontend Interview Answers (AI Engineer | 4 Years Experience)

> **Profile:** AI Engineer with 4 years of experience. My primary expertise is in Python, FastAPI, Generative AI, and backend development. I have also worked with React for building AI dashboards, chatbot UIs, and integrating frontend applications with REST APIs.

---

# React

## 1. What are React Hooks?

React Hooks are built-in functions introduced in React 16.8 that allow functional components to use state and lifecycle features without writing class components.

### Common Hooks

### `useState`

Used to manage component state.

```javascript
import { useState } from "react";

function Counter() {
    const [count, setCount] = useState(0);

    return (
        <button onClick={() => setCount(count + 1)}>
            {count}
        </button>
    );
}
```

---

### `useEffect`

Used for side effects such as API calls, subscriptions, and timers.

```javascript
useEffect(() => {
    fetchUsers();
}, []);
```

---

### `useContext`

Used to share data across components without prop drilling.

---

### `useRef`

Used to reference DOM elements or persist mutable values across renders.

---

### `useMemo`

Optimizes expensive calculations by memoizing computed values.

---

### `useCallback`

Memoizes functions to avoid unnecessary re-renders.

---

### Real-world Usage

In AI applications, I have used React Hooks for:

- Calling FastAPI APIs
- Managing chatbot conversations
- Uploading PDFs
- Displaying AI responses
- Managing authentication state
- Handling loading indicators

---

## 2. What are Sessions and Cookies in React?

React itself does not manage sessions or cookies. These are handled by the browser and backend.

### Cookies

Cookies are small pieces of data stored in the browser and sent with every request to the server.

Common uses:

- Authentication tokens
- User preferences
- Remember Me functionality

Example:

```javascript
document.cookie = "username=John";
```

---

### Sessions

A session stores user-specific data on the server, while the browser stores only a session identifier (Session ID) in a cookie.

Example:

```
Browser
   │
Session ID
   │
Server
   │
User Data
```

---

### Difference

| Cookies | Sessions |
|----------|-----------|
| Stored in browser | Stored on server |
| Limited storage | Larger storage |
| Less secure | More secure |
| Sent with every request | Accessed using Session ID |

---

### Real-world Usage

In AI applications, authentication is typically implemented using:

- JWT Tokens
- HTTP-only Cookies
- Redis-backed Sessions
- OAuth providers (Google, Microsoft)

---

## 3. Can We Transfer Session Data from One Session to Another?

Directly transferring session data between two independent sessions is **not recommended** because each session has a unique Session ID.

However, user state can be shared using:

- JWT Authentication
- Database persistence
- Redis
- Shared cache
- Local Storage (for non-sensitive data)
- Secure Cookies

### Example

User logs in from another device:

```
User
   │
JWT Token
   │
Backend
   │
Database
```

The backend retrieves the user's information using the token instead of copying the previous session.

---

# Angular

## 4. What is the Angular Lifecycle?

Angular components go through different lifecycle stages from creation to destruction.

### Common Lifecycle Hooks

### `ngOnChanges()`

Called when input properties change.

---

### `ngOnInit()`

Called once after component initialization.

Used for:

- API calls
- Variable initialization
- Fetching data

---

### `ngDoCheck()`

Called during every change detection cycle.

---

### `ngAfterContentInit()`

Called after projected content is initialized.

---

### `ngAfterViewInit()`

Called after component views and child views are initialized.

---

### `ngOnDestroy()`

Called before the component is destroyed.

Used for:

- Cleaning subscriptions
- Removing event listeners
- Clearing timers

---

### Lifecycle Flow

```
Constructor
      ↓
ngOnChanges
      ↓
ngOnInit
      ↓
ngDoCheck
      ↓
ngAfterContentInit
      ↓
ngAfterViewInit
      ↓
ngOnDestroy
```

---

# General Frontend

## 5. Do You Know JavaScript?

Yes.

Although my primary role is AI and backend development, I have experience using JavaScript to build AI-powered web applications and integrate frontend interfaces with backend APIs.

### JavaScript Concepts I Have Worked With

- Variables (`let`, `const`)
- Functions
- Arrow Functions
- Objects and Arrays
- ES6 Features
- Promises
- Async/Await
- Fetch API
- DOM Manipulation
- Event Handling
- Modules
- JSON
- Closures
- Higher-Order Functions

### Example

```javascript
async function fetchData() {
    const response = await fetch("/api/chat");
    const data = await response.json();
    console.log(data);
}
```

### Real-world Usage

I have used JavaScript to:

- Build React-based chatbot interfaces
- Integrate FastAPI REST APIs
- Upload PDFs and images
- Display streaming LLM responses
- Handle authentication
- Consume WebSocket APIs
- Build AI dashboards and admin portals

> **Interview Tip:** Since your primary expertise is AI Engineering, it's perfectly acceptable to mention that your frontend experience is focused on integrating AI applications rather than building large-scale frontend systems from scratch.