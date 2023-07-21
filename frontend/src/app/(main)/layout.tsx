import Nav from '@app/components/nav';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Nav></Nav>
      <main className="flex-grow">{children}</main>
    </>
  );
}
