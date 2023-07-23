import Nav from '@app/_components/nav';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <Nav></Nav>
      {children}
    </div>
  );
}
