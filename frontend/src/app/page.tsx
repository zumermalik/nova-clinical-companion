"use client";

import React, { useState } from 'react';
import axios from 'axios';
import { Mic, UploadCloud, Activity, FileText, Send, BrainCircuit, Loader2, CheckCircle2, Database } from 'lucide-react';

// YOUR SPECIFIC CODESPACE BACKEND URL
const API_BASE_URL = "https://ominous-zebra-6959qxxj6j6xc4pgx-8000.app.github.dev";

export default function Dashboard() {
  const [noteText, setNoteText] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [reasoningResult, setReasoningResult] = useState("");
  const [syncStatus, setSyncStatus] = useState("Idle");

  // Toggle Voice Recording
  const toggleRecording = () => {
    setIsRecording(!isRecording);
    if (!isRecording) {
      setNoteText("Patient John Doe, 45 years old, presents with a severe migraine. Prescribed 400mg Ibuprofen and advised to rest in a dark room.");
    }
  };

  // THE REAL AWS NOVA CONNECTION
  const handleProcessNote = async () => {
    if (!noteText) return;
    setIsProcessing(true);
    setReasoningResult("");

    try {
      // Sending the text to our Python backend, which routes to Nova 2 Lite
      const response = await axios.post(`${API_BASE_URL}/api/agent/process-note`, {
        text: noteText
      });
      setReasoningResult(response.data.structured_data);
    } catch (error) {
      console.error("API Error:", error);
      setReasoningResult("⚠️ Error connecting to Nova API. Is the Python backend running and the port public?");
    } finally {
      setIsProcessing(false);
    }
  };

  const handleSync = () => {
    setSyncStatus("Syncing...");
    setTimeout(() => setSyncStatus("Synced"), 1500);
  };

  return (
    <div className="min-h-screen bg-[#0a0a0f] text-slate-300 font-sans selection:bg-purple-500/30">
      
      {/* TOP NAVIGATION */}
      <nav className="border-b border-slate-800/60 bg-[#0f0f16] px-6 py-4 flex justify-between items-center sticky top-0 z-10">
        <div className="flex items-center gap-3">
          <div className="bg-purple-600 p-2 rounded-lg shadow-lg shadow-purple-900/20">
            <Activity className="text-white w-5 h-5" />
          </div>
          <span className="text-xl font-semibold text-slate-100 tracking-tight">Nova Clinical</span>
        </div>
        <div className="flex items-center gap-2 text-xs font-medium text-emerald-400 bg-emerald-400/10 px-3 py-1.5 rounded-full border border-emerald-400/20">
          <div className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></div>
          Nova System Active
        </div>
      </nav>

      {/* MAIN WORKSPACE */}
      <main className="max-w-6xl mx-auto p-6 mt-4 grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* LEFT PANEL: Input (Dictation & Vision) */}
        <div className="col-span-1 lg:col-span-5 space-y-6">
          
          {/* Audio Input Card */}
          <div className="bg-[#13131c] border border-slate-800/60 rounded-xl overflow-hidden shadow-xl">
            <div className="px-5 py-4 border-b border-slate-800/60 bg-[#161622] flex items-center justify-between">
              <h2 className="text-sm font-semibold text-slate-200 flex items-center gap-2">
                <Mic className="w-4 h-4 text-purple-400" /> Dictation (Nova Sonic)
              </h2>
            </div>
            <div className="p-5 space-y-4">
              <textarea 
                className="w-full bg-[#0a0a0f] border border-slate-700/50 rounded-lg p-4 text-sm text-slate-200 h-32 focus:outline-none focus:border-purple-500/50 focus:ring-1 focus:ring-purple-500/50 transition-all resize-none placeholder-slate-600"
                placeholder="Click the mic to start hands-free dictation..."
                value={noteText}
                onChange={(e) => setNoteText(e.target.value)}
              />
              <button 
                onClick={toggleRecording}
                className={`w-full py-2.5 rounded-lg flex items-center justify-center gap-2 text-sm font-medium transition-all ${isRecording ? 'bg-red-500/10 text-red-400 border border-red-500/20' : 'bg-[#1e1e2d] hover:bg-[#252536] text-slate-300 border border-slate-700/50'}`}
              >
                <Mic className="w-4 h-4" /> {isRecording ? "Stop Recording" : "Tap to Dictate"}
              </button>
            </div>
          </div>

          {/* Vision Input Card */}
          <div className="bg-[#13131c] border border-slate-800/60 rounded-xl overflow-hidden shadow-xl">
             <div className="px-5 py-4 border-b border-slate-800/60 bg-[#161622]">
              <h2 className="text-sm font-semibold text-slate-200 flex items-center gap-2">
                <UploadCloud className="w-4 h-4 text-purple-400" /> Literature & Labs (Nova Vision)
              </h2>
            </div>
            <div className="p-5">
              <div className="border border-dashed border-slate-700/50 rounded-lg py-8 text-center hover:bg-[#1a1a24] hover:border-purple-500/30 transition-all cursor-pointer group">
                <FileText className="w-8 h-8 text-slate-600 mx-auto mb-2 group-hover:text-purple-400 transition-colors" />
                <p className="text-sm text-slate-400">Upload PDFs or X-Rays for analysis</p>
              </div>
            </div>
          </div>
        </div>

        {/* RIGHT PANEL: Output (Agentic Reasoning & EHR Sync) */}
        <div className="col-span-1 lg:col-span-7 space-y-6 flex flex-col">
          
          {/* Agentic Output Card */}
          <div className="bg-[#13131c] border border-slate-800/60 rounded-xl overflow-hidden shadow-xl flex-grow flex flex-col">
            <div className="px-5 py-4 border-b border-slate-800/60 bg-[#161622] flex items-center justify-between">
              <h2 className="text-sm font-semibold text-slate-200 flex items-center gap-2">
                <BrainCircuit className="w-4 h-4 text-purple-400" /> Structured Data (Nova Lite)
              </h2>
              <button 
                onClick={handleProcessNote}
                disabled={!noteText || isProcessing}
                className="bg-purple-600 hover:bg-purple-500 disabled:opacity-50 disabled:cursor-not-allowed text-white text-xs px-4 py-1.5 rounded-md flex items-center gap-2 font-medium transition-colors"
              >
                {isProcessing ? <Loader2 className="w-3 h-3 animate-spin" /> : <BrainCircuit className="w-3 h-3" />}
                {isProcessing ? "Processing..." : "Run AI Parsing"}
              </button>
            </div>
            
            <div className="p-5 flex-grow flex flex-col">
              {reasoningResult ? (
                <div className="bg-[#0a0a0f] border border-purple-900/30 rounded-lg p-5 flex-grow text-sm text-purple-100/90 whitespace-pre-wrap font-mono shadow-inner leading-relaxed">
                  {reasoningResult}
                </div>
              ) : (
                <div className="flex-grow flex items-center justify-center text-slate-600 text-sm border border-dashed border-slate-800/50 rounded-lg">
                  Run the agent to extract medical entities...
                </div>
              )}
            </div>
          </div>

          {/* UI Automation Card */}
          <div className="bg-[#13131c] border border-slate-800/60 rounded-xl overflow-hidden shadow-xl">
             <div className="px-5 py-4 border-b border-slate-800/60 bg-[#161622] flex items-center justify-between">
              <h2 className="text-sm font-semibold text-slate-200 flex items-center gap-2">
                <Database className="w-4 h-4 text-purple-400" /> EHR Automation (Nova Act)
              </h2>
            </div>
            <div className="p-5 flex items-center justify-between">
              <p className="text-sm text-slate-400">Push structured entities to target database.</p>
              <button 
                onClick={handleSync}
                disabled={!reasoningResult || syncStatus === "Syncing..."}
                className="bg-slate-800 hover:bg-slate-700 disabled:opacity-50 text-slate-200 text-sm px-5 py-2 rounded-lg flex items-center gap-2 transition-colors font-medium border border-slate-700"
              >
                {syncStatus === "Synced" ? <CheckCircle2 className="w-4 h-4 text-emerald-400" /> : <Send className="w-4 h-4" />}
                {syncStatus}
              </button>
            </div>
          </div>

        </div>
      </main>
    </div>
  );
}