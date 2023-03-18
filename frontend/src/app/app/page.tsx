import BookingPage from '@components/booking-page';
import { Site } from 'src/types/types';
import { fetchSites } from 'src/utils/api';

async function getSites(): Promise<Site[]> {
  const res = await fetchSites();

  if (!res.ok) {
    throw new Error(res.status + ' ' + 'Failed to fetch bookings');
  }

  return res.json();
}

export default async function Home() {
  const sites = await getSites();

  return (
    <div className="mx-auto mt-6 mb-6 max-w-lg px-3">
      <BookingPage sites={sites} />
    </div>
  );
}
