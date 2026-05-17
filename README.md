<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:0a192f,100:112240&height=200&section=header&text=Manmay%20Chakraborty&fontSize=56&fontColor=ccd6f6&animation=fadeIn&fontAlignY=40&desc=Backend%20Engineer%20%E2%80%A2%20Systems%20Thinker%20%E2%80%A2%20AI%20Builder&descAlignY=62&descSize=16&descColor=64ffda" />

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1400&color=64FFDA&center=true&vCenter=true&width=680&lines=Building+real-time+systems+in+Node.js+%26+Go;Full-stack+with+a+backend+bias;LangChain+%2B+FastAPI+%2B+biomedical+data+%E2%86%92+shipped+in+24h;Open+to+backend+%2F+AI+internships+globally+%F0%9F%9A%80" />

<br/><br/>

<a href="https://linkedin.com/in/imanmay2"><img src="https://img.shields.io/badge/LinkedIn-0a192f?style=for-the-badge&logo=linkedin&logoColor=64ffda"/></a>
&nbsp;
<a href="mailto:imanmay2@gmail.com"><img src="https://img.shields.io/badge/imanmay2@gmail.com-0a192f?style=for-the-badge&logo=gmail&logoColor=64ffda"/></a>
&nbsp;
<a href="https://github.com/imanmay2"><img src="https://img.shields.io/badge/GitHub-0a192f?style=for-the-badge&logo=github&logoColor=64ffda"/></a>
&nbsp;
<a href="https://leetcode.com/imanmay2"><img src="https://img.shields.io/badge/LeetCode-0a192f?style=for-the-badge&logo=leetcode&logoColor=64ffda"/></a>

</div>

---

```ts
const manmay = {
  focus:    "backend systems, real-time infra, AI integration",
  degree:   "B.Tech CSE (AI & ML) — VIT Chennai, 2028",
  now:      "building NexCare, a telemedicine platform with video + pharmacy workflows",
  looking:  "backend / AI internships — available from May 2026",
  belief:   "a well-designed API is better than a pretty UI",
};
```

I'm a backend-heavy full-stack developer who prefers designing systems over cloning tutorials.
Most of my time goes into thinking about how data flows, where things break under load, and how to make services talk to each other without a mess.
I work primarily in **Node.js** and **Go** on the backend, use **React/Next.js** when the frontend actually needs me, and reach for **LangChain + FastAPI** when there's an AI problem worth solving.

---

## 🚀 Projects

> Things I built to solve actual problems, not to pad a portfolio.

---

### NexCare — Telemedicine Platform
`Node.js` `WebRTC` `WebSockets` `PostgreSQL` `Redis` `Docker`

Full-stack telemedicine system with real-time video consultations, asynchronous prescription management, and a pharmacy workflow that tracks medication status from prescription to dispensing.

The interesting engineering problems: WebRTC signalling under unreliable network conditions, session state across disconnects, and keeping the pharmacy queue consistent without a race condition when multiple pharmacists are online.

**Status:** Active development &nbsp;|&nbsp; [Repo →](https://github.com/imanmay2)

---

### iChat — Real-Time Chat Infrastructure
`Node.js` `WebSockets` `WebRTC` `Redis Pub/Sub` `MongoDB`

Real-time chat application built to understand the actual mechanics of WebSocket connection management — not just `socket.emit()`. Implemented Redis Pub/Sub for horizontal scaling so sessions on different server instances can communicate, and WebRTC for peer-to-peer voice.

The goal was to understand what breaks when you move from 1 server to 3.

**Status:** Complete &nbsp;|&nbsp; [Repo →](https://github.com/imanmay2)

---

### PharmaMind — AI Drug Repurposing Research Tool
`FastAPI` `LangChain` `React` `MongoDB` `Plotly` `Recharts`

Built in 24 hours at a hackathon. Agentic AI system that takes a disease query, hits biomedical databases (PubMed, ChEMBL), and surfaces drug-repurposing candidates with evidence summaries. LangChain agents handle query decomposition and source aggregation; Plotly renders the compound relationship graphs.

This was the project that made me take LLM tool-use seriously.

**Status:** Hackathon build &nbsp;|&nbsp; [Repo →](https://github.com/imanmay2)

---

### QNeX — Quiz Platform with Shareable Test IDs
`MongoDB` `Express.js` `React` `Node.js` `Cohere AI`

Quiz platform where you create a test and share a unique ID — anyone with the link takes the same test instance. Cohere AI generates questions from a topic + difficulty input. Built proper analytics (per-user scores, question-level accuracy, time-per-question) rather than just showing a final number.

The schema design for tracking attempts without duplicating question data was the most interesting part.

**Status:** Complete &nbsp;|&nbsp; [Repo →](https://github.com/imanmay2)

---

### WanderLust — Listings & Booking Platform
`Node.js` `Express.js` `MongoDB` `Mapbox API` `Passport.js`

Yes, it's an Airbnb-style app. But the point wasn't the idea — it was getting comfortable with geospatial queries, RESTful resource design, and authentication flows (session vs token, CSRF handling). Mapbox integration for radius-based listing search was the non-tutorial part.

**Status:** Complete &nbsp;|&nbsp; [Repo →](https://github.com/imanmay2)

---

## 🛠️ Stack

I use what solves the problem. These are the tools I'm actually comfortable with:

<div align="center">

![Skills](https://skillicons.dev/icons?i=nodejs,go,python,react,nextjs,ts,postgres,mongodb,redis,docker,linux,git&perline=12)

</div>

<br/>

**Backend** &nbsp; `Node.js` `Express.js` `Go (Gin)` `FastAPI` `WebSockets` `REST` `gRPC (learning)`

**Frontend** &nbsp; `React` `Next.js` `TypeScript` `Tailwind CSS`

**Data** &nbsp; `PostgreSQL` `MongoDB` `Redis` `Supabase` `MySQL`

**Infrastructure** &nbsp; `Docker` `CI/CD (GitHub Actions)` `Linux`

**AI / ML** &nbsp; `LangChain` `Cohere AI` `FastAPI` `Python`

**Languages** &nbsp; `JavaScript` `TypeScript` `Go` `Python` `C++` `Java`

---

## 📍 Currently

- 🏗️ Building **NexCare** — telemedicine + pharmacy workflow platform
- 📖 Going deeper into **distributed systems** — consensus, replication, partition tolerance
- ⚙️ Learning **gRPC** for inter-service communication in Go
- 🌍 Actively applying for **backend / AI engineering internships** — available from **May 2026**

---

## 💼 Experience

**Software Engineer Intern — Cestrum Technologies** *(Nov 2025 – Feb 2026)*
Built WebSocket backend for real-time communication — connection lifecycle management, message broadcasting across concurrent sessions, and server-side event processing. First time I had to care about what happens at 500 simultaneous connections, not just 5.

**Web Development Lead — CodeChef VIT Chennai** *(Jul 2025 – Present)*
Led backend for SIH 2025 team project in Go + Next.js + MongoDB. Mentored juniors on API design and database schema decisions.

**Technical Team — E-Cell VIT Chennai** *(Aug 2025 – Apr 2026)*
Built a real-time Stock Market Simulator — live price indicators, interactive trading UI, event-state synchronization.

---

## ⏱️ Weekly Coding Breakdown

<!--START_SECTION:waka-->
> Set up [WakaTime](https://wakatime.com) + the [waka-readme](https://github.com/athul/waka-readme) GitHub Action to auto-populate live coding stats here.
<!--END_SECTION:waka-->

---

## 📊 GitHub Stats

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=imanmay2&show_icons=true&theme=transparent&hide_border=true&title_color=64ffda&icon_color=64ffda&text_color=8892b0&bg_color=0d1117&count_private=true&include_all_commits=true"/>
<img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user=imanmay2&theme=transparent&hide_border=true&stroke=64ffda&ring=64ffda&fire=ff6b6b&currStreakLabel=64ffda&sideLabels=8892b0&dates=8892b0&background=0d1117"/>

<br/><br/>

<img width="42%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=imanmay2&layout=compact&theme=transparent&hide_border=true&title_color=64ffda&text_color=8892b0&bg_color=0d1117&langs_count=6&hide=html,css"/>

</div>

---

## 📈 Activity

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=imanmay2&bg_color=0d1117&color=64ffda&line=64ffda&point=ccd6f6&area=true&area_color=112240&hide_border=true"/>
</div>

---

## 🏆 Trophies

<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=imanmay2&theme=radical&no-frame=true&no-bg=true&margin-w=6&column=7"/>
</div>

---

## 📬 Contact

If you're building something interesting in backend infrastructure, real-time systems, or AI tooling — and you need someone who'll figure things out rather than wait to be told what to do — reach out.

**imanmay2@gmail.com** &nbsp;|&nbsp; [LinkedIn](https://linkedin.com/in/imanmay2) &nbsp;|&nbsp; Available from **May 2026**

---

<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:112240,100:0d1117&height=120&section=footer"/>
</div>
