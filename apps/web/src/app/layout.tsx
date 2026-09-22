import type { ReactNode } from "react";
export const metadata = { title: "PSiron2.1", description: "Evidence-driven security assessment platform" };
export default function RootLayout({children}:{children:ReactNode}) { return <html lang="en"><body style={{margin:0,background:"#070b12",color:"#e6edf3",fontFamily:"ui-monospace, SFMono-Regular, Menlo, monospace"}}>{children}</body></html>; }
