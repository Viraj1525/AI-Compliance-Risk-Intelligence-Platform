import { useLocation } from 'react-router-dom';
import { Shield, Activity } from 'lucide-react';

const routeTitles = {
    '/': { title: 'Dashboard', subtitle: 'Overview of compliance health' },
    '/upload': { title: 'Upload Documents', subtitle: 'Add enterprise PDFs & policies' },
    '/analyze': { title: 'Risk Analysis', subtitle: 'AI-powered compliance detection' },
    '/chat': { title: 'AI Chat', subtitle: 'Converse with your documents' },
    '/report': { title: 'Compliance Report', subtitle: 'Generate & download audit reports' },
};

export default function Topbar() {
    const location = useLocation();
    const matched = Object.keys(routeTitles)
        .sort((a, b) => b.length - a.length)
        .find((k) => location.pathname === k || location.pathname.startsWith(k));
    const info = routeTitles[matched] || routeTitles['/'];

    return (
        <header
            style={{
                height: 68,
                background: 'rgba(15, 23, 42, 0.85)',
                backdropFilter: 'blur(12px)',
                borderBottom: '1px solid var(--border)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '0 28px',
                position: 'sticky',
                top: 0,
                zIndex: 50,
            }}
        >
            {/* Left: title */}
            <div>
                <h1 style={{ fontSize: '1.05rem', fontWeight: 700, fontFamily: 'Outfit', color: 'var(--text-primary)', lineHeight: 1.3 }}>
                    {info.title}
                </h1>
                <p style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', marginTop: 1 }}>
                    {info.subtitle}
                </p>
            </div>

            {/* Right: status badge */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 8,
                    background: 'rgba(16,185,129,0.1)',
                    border: '1px solid rgba(16,185,129,0.25)',
                    borderRadius: 999,
                    padding: '6px 14px',
                }}>
                    <span style={{ width: 7, height: 7, borderRadius: '50%', background: '#10b981', boxShadow: '0 0 8px #10b981', display: 'inline-block' }} />
                    <span style={{ fontSize: '0.75rem', color: '#34d399', fontWeight: 600 }}>Platform Active</span>
                </div>
                <div style={{
                    width: 36, height: 36,
                    background: 'linear-gradient(135deg, #3b82f6, #06b6d4)',
                    borderRadius: 10,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    boxShadow: '0 2px 10px rgba(59,130,246,0.3)',
                    cursor: 'pointer',
                }}>
                    <Shield size={17} color="white" strokeWidth={2.5} />
                </div>
            </div>
        </header>
    );
}

