<div align="center">
  <img src="assets/hero.svg" width="100%" alt="Manmay Chakraborty — Backend Engineer · Systems Thinker · AI Builder"/>
</div>

<div align="center">

<a href="https://linkedin.com/in/imanmay2"><img src="https://img.shields.io/badge/LinkedIn-0a192f?style=for-the-badge&logo=linkedin&logoColor=64ffda&labelColor=0d1117" alt="LinkedIn"/></a>
<a href="mailto:imanmay2@gmail.com"><img src="https://img.shields.io/badge/Email-0a192f?style=for-the-badge&logo=gmail&logoColor=64ffda&labelColor=0d1117" alt="Email"/></a>
<a href="https://github.com/imanmay2"><img src="https://img.shields.io/badge/GitHub-0a192f?style=for-the-badge&logo=github&logoColor=64ffda&labelColor=0d1117" alt="GitHub"/></a>
<img src="https://img.shields.io/badge/Chennai,%20IN-0a192f?style=for-the-badge&logo=googlemaps&logoColor=64ffda&labelColor=0d1117" alt="Chennai, India"/>
<img src="https://img.shields.io/badge/Open%20from%20May%202026-0a192f?style=for-the-badge&logo=googlecalendar&logoColor=64ffda&labelColor=0d1117" alt="Available from May 2026"/>

<br/>

<img src="https://komarev.com/ghpvc/?username=imanmay2&style=flat-square&color=64ffda&label=PROFILE+VIEWS" alt="Profile views"/>
<a href="https://github.com/imanmay2?tab=followers"><img src="https://img.shields.io/github/followers/imanmay2?style=flat-square&color=64ffda&labelColor=0d1117&label=FOLLOWERS" alt="Followers"/></a>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&pause=1400&color=64FFDA&center=true&vCenter=true&width=700&height=40&lines=Real-time+systems+in+Node.js+and+Go;LangChain+%2B+FastAPI+over+biomedical+data%2C+shipped+in+24h;WebSockets%2C+WebRTC%2C+and+state+that+survives+a+disconnect;A+well-designed+API+beats+a+pretty+UI" alt="What I build"/>

</div>

<br/>

---

## `$ whoami`

<img align="right" width="262" src="assets/portrait.svg" alt="ASCII portrait of Manmay Chakraborty"/>

I'm a backend-heavy full-stack developer who'd rather design a system than clone a tutorial.

Most of my time goes into how data flows, where things break under load, and how services talk to each
other without turning into a mess. I work primarily in **Node.js** and **Go**, reach for **React/Next.js**
when the frontend actually needs me, and pull in **LangChain + FastAPI** when there's an AI problem worth solving.

The thing I care about most: what happens on the **unhappy path** — the dropped connection, the duplicate
write, the third pharmacist who clicked at the same moment.

<br clear="right"/>

```ts
const manmay = {
  focus:   ["backend systems", "real-time infra", "AI integration"],
  degree:  "B.Tech CSE (AI & ML) · VIT Chennai · 2028",
  now:     "NexCare — telemedicine with video consults + pharmacy workflows",
  reading: "distributed systems: consensus, replication, partition tolerance",
  open:    { role: "backend / AI internships", from: "May 2026" },
  belief:  "a well-designed API is better than a pretty UI",
} as const;
```

<sub>The portrait above is my actual photograph, not hand-drawn — luminance remapped through a levels
pass, background dropped with a feathered elliptical mask, then quantised onto a ten-character ramp.
Generator: <a href="assets/ascii_portrait.py">assets/ascii_portrait.py</a>.</sub>

---

## `$ ls ~/systems`

> Things I built to solve actual problems, not to pad a portfolio.

### ⬢ &nbsp;NexCare — Telemedicine Platform

<img src="https://img.shields.io/badge/Go-0d1117?style=flat-square&logo=go&logoColor=64ffda"/> <img src="https://img.shields.io/badge/WebRTC-0d1117?style=flat-square&logo=webrtc&logoColor=64ffda"/> <img src="https://img.shields.io/badge/WebSockets-0d1117?style=flat-square&logo=socketdotio&logoColor=64ffda"/> <img src="https://img.shields.io/badge/PostgreSQL-0d1117?style=flat-square&logo=postgresql&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Redis-0d1117?style=flat-square&logo=redis&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Docker-0d1117?style=flat-square&logo=docker&logoColor=64ffda"/>

Real-time video consultations, asynchronous prescription management, and a pharmacy workflow that tracks
medication from prescription through to dispensing.

<details>
<summary><b>Engineering notes</b></summary>

<br/>

```
  patient ──ws──┐                          ┌── signalling (SDP / ICE)
                ├─▶  gateway (Go)  ──┬──▶  │
  doctor  ──ws──┘        │           │     └── session store (Redis)
                         │           │
                         ▼           └──▶  prescription svc ──▶ Postgres
                   presence + reconnect                              │
                                                                     ▼
                                              pharmacy queue ── SELECT … FOR UPDATE
```

The problems that actually took thinking:

- **WebRTC signalling on bad networks** — ICE restarts and renegotiation so a consult survives a
  patient walking out of Wi-Fi range, instead of dropping the call.
- **Session state across disconnects** — presence and call state in Redis with TTLs, so a reconnect
  rejoins the same room rather than starting a ghost session.
- **The pharmacy race** — several pharmacists online, one prescription. Row-level locking so a
  medication can't be dispensed twice, and the queue stays consistent under concurrent claims.

</details>

**Status:** active development &nbsp;·&nbsp; [**Repo →**](https://github.com/imanmay2/NexCare)

<br/>

### ⬢ &nbsp;PharmaMind — AI Drug-Repurposing Research Tool

<img src="https://img.shields.io/badge/FastAPI-0d1117?style=flat-square&logo=fastapi&logoColor=64ffda"/> <img src="https://img.shields.io/badge/LangChain-0d1117?style=flat-square&logo=langchain&logoColor=64ffda"/> <img src="https://img.shields.io/badge/React-0d1117?style=flat-square&logo=react&logoColor=64ffda"/> <img src="https://img.shields.io/badge/MongoDB-0d1117?style=flat-square&logo=mongodb&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Plotly-0d1117?style=flat-square&logo=plotly&logoColor=64ffda"/>

Built in 24 hours at a hackathon. An agentic system that takes a disease query, hits biomedical databases
(PubMed, ChEMBL), and surfaces drug-repurposing candidates with evidence summaries.

<details>
<summary><b>Engineering notes</b></summary>

<br/>

LangChain agents handle query decomposition and source aggregation; Plotly renders the compound
relationship graphs. The interesting part wasn't the prompting — it was **bounding the agent**:
capping tool-call depth, deduplicating overlapping literature hits, and keeping every claim traceable
back to a source so the output is auditable rather than plausible-sounding.

This was the project that made me take LLM tool-use seriously.

</details>

**Status:** hackathon build &nbsp;·&nbsp; [**Repo →**](https://github.com/imanmay2/PharmaMind)

<br/>

### ⬢ &nbsp;QNeX — Quiz Platform with Shareable Test IDs

<img src="https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=nodedotjs&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Express-0d1117?style=flat-square&logo=express&logoColor=64ffda"/> <img src="https://img.shields.io/badge/React-0d1117?style=flat-square&logo=react&logoColor=64ffda"/> <img src="https://img.shields.io/badge/MongoDB-0d1117?style=flat-square&logo=mongodb&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Cohere-0d1117?style=flat-square&logo=cohere&logoColor=64ffda"/>

Create a test, share one ID, and everyone with the link takes the same instance. Cohere generates the
questions from a topic + difficulty input.

<details>
<summary><b>Engineering notes</b></summary>

<br/>

Real analytics rather than a final score: per-user results, question-level accuracy, and time-per-question.
The interesting part was the **schema** — modelling attempts as references into a single immutable question
set, so thousands of attempts don't duplicate question data and an edit to a test never silently rewrites
history for people who already took it.

</details>

**Status:** complete &nbsp;·&nbsp; [**Repo →**](https://github.com/imanmay2/QNeX)

<br/>

### ⬢ &nbsp;WanderLust — Listings & Booking Platform

<img src="https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=nodedotjs&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Express-0d1117?style=flat-square&logo=express&logoColor=64ffda"/> <img src="https://img.shields.io/badge/MongoDB-0d1117?style=flat-square&logo=mongodb&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Mapbox-0d1117?style=flat-square&logo=mapbox&logoColor=64ffda"/> <img src="https://img.shields.io/badge/Passport.js-0d1117?style=flat-square&logo=passport&logoColor=64ffda"/>

Yes, it's an Airbnb-style app — the idea was never the point. Geospatial queries, RESTful resource design,
and auth flows (session vs. token, CSRF handling) were. Radius-based listing search via Mapbox was the
non-tutorial part.

**Status:** complete &nbsp;·&nbsp; [**Repo →**](https://github.com/imanmay2/wander_lust)

---

## `$ cat stack.toml`

<div align="center">
  <img src="https://skillicons.dev/icons?i=go,nodejs,python,ts,react,nextjs,fastapi,postgres,mongodb,redis,docker,linux,git,tailwind&perline=14" alt="Tech stack"/>
</div>

<br/>

| | |
|:--|:--|
| **Backend** | `Go (Gin)` · `Node.js` · `Express` · `FastAPI` · `WebSockets` · `WebRTC` · `REST` · `gRPC` *(learning)* |
| **Frontend** | `React` · `Next.js` · `TypeScript` · `Tailwind CSS` |
| **Data** | `PostgreSQL` · `MongoDB` · `Redis` · `Supabase` · `MySQL` |
| **Infra** | `Docker` · `GitHub Actions` · `Linux` |
| **AI** | `LangChain` · `Cohere` · `FastAPI` · `Python` |
| **Languages** | `Go` · `TypeScript` · `JavaScript` · `Python` · `Java` · `C++` |

---

## `$ git log --author="manmay"`

**Software Engineer Intern** — *Cestrum Technologies* &nbsp;<sub>`Nov 2025 → Feb 2026`</sub>
> Built the WebSocket backend for real-time communication: connection lifecycle management, message
> broadcasting across concurrent sessions, server-side event processing. First time I had to care what
> happens at 500 simultaneous connections, not 5.

**Web Development Lead** — *CodeChef VIT Chennai* &nbsp;<sub>`Jul 2025 → present`</sub>
> Led backend for the SIH 2025 team project in Go + Next.js + MongoDB. Mentored juniors on API design
> and schema decisions — mostly on why the boring choice is usually right.

**Technical Team** — *E-Cell VIT Chennai* &nbsp;<sub>`Aug 2025 → Apr 2026`</sub>
> Built a real-time Stock Market Simulator: live price indicators, interactive trading UI, event-state
> synchronisation across clients.

---

## `$ top -o commits`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=imanmay2&hide_border=true&background=0d1117&stroke=64ffda&ring=64ffda&fire=ff6b6b&currStreakLabel=64ffda&sideLabels=8892b0&dates=8892b0&currStreakNum=ccd6f6&sideNums=ccd6f6"/>
  <img width="48%" src="https://streak-stats.demolab.com?user=imanmay2&hide_border=true&background=ffffff&stroke=0a7f6b&ring=0a7f6b&fire=ff6b6b&currStreakLabel=0a7f6b" alt="Contribution streak"/>
</picture>
<img width="48%" src="assets/langs.svg" alt="Most used languages"/>

</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/imanmay2/imanmay2/output/snake-dark.svg"/>
    <img width="100%" src="https://raw.githubusercontent.com/imanmay2/imanmay2/output/snake.svg" alt="A snake eating my contribution graph"/>
  </picture>
</div>

---

## `$ mail -s "hello"`

If you're building something in **backend infrastructure, real-time systems, or AI tooling** — and you want
someone who'll go figure it out rather than wait to be told what to do — I'd like to hear about it.

<div align="center">

<br/>

<a href="mailto:imanmay2@gmail.com"><img src="https://img.shields.io/badge/imanmay2@gmail.com-0a192f?style=for-the-badge&logo=gmail&logoColor=64ffda&labelColor=0d1117"/></a>
<a href="https://linkedin.com/in/imanmay2"><img src="https://img.shields.io/badge/linkedin.com/in/imanmay2-0a192f?style=for-the-badge&logo=linkedin&logoColor=64ffda&labelColor=0d1117"/></a>

<br/><br/>

<sub><i>Available from May 2026 · open to relocation</i></sub>

</div>

<img width="100%" src="assets/footer.svg" alt=""/>
