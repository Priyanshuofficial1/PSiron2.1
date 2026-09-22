"use client";
import { useState } from "react";
export default function Home() {
  const [target,setTarget]=useState("");
  const [status,setStatus]=useState("READY");
  async function createAssessment() {
    if (!target.trim()) return setStatus("TARGET_REQUIRED");
    setStatus("VALIDATING_SCOPE");
    try {
      const r=await fetch((process.env.NEXT_PUBLIC_API_URL||"http://localhost:8000")+"/v1/targets",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({kind:"url",value:target})});
      setStatus(r.ok?"TARGET_ACCEPTED":"API_ERROR");
    } catch { setStatus("API_UNAVAILABLE"); }
  }
  return <main style={{minHeight:"100vh",padding:"40px",boxSizing:"border-box"}}>
    <header style={{display:"flex",justifyContent:"space-between",borderBottom:"1px solid #263241",paddingBottom:18}}>
      <div><strong style={{fontSize:24}}>PSiron2.1</strong><div style={{opacity:.65,fontSize:12}}>EVIDENCE-DRIVEN SECURITY ASSESSMENT</div></div>
      <div style={{fontSize:12}}>ENGINE: DETERMINISTIC · AI RUNTIME: OFF</div>
    </header>
    <section style={{maxWidth:1000,margin:"70px auto"}}>
      <div style={{fontSize:12,opacity:.6}}>ASSESSMENT CONTROL PLANE</div>
      <h1 style={{fontSize:48,margin:"10px 0"}}>DISCOVER. VERIFY. PROVE.</h1>
      <p style={{opacity:.75,maxWidth:720}}>Create a scoped assessment, execute applicable security capabilities, preserve evidence, correlate observations and verify findings without treating scanner output as proof.</p>
      <div style={{display:"flex",gap:10,marginTop:35}}>
        <input value={target} onChange={e=>setTarget(e.target.value)} placeholder="https://authorized-target.example" style={{flex:1,padding:16,background:"#0d131c",border:"1px solid #334155",color:"white"}} />
        <button onClick={createAssessment} style={{padding:"0 22px",background:"#dbeafe",border:0,cursor:"pointer"}}>CREATE ASSESSMENT</button>
      </div>
      <div style={{marginTop:18,fontSize:12}}>STATUS: {status}</div>
    </section>
  </main>
}
