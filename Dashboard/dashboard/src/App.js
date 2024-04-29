import React, {useState,useEffect} from 'react';
import { DataTable } from '@carbon/react';


const {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableHeader,
  TableRow
} = DataTable;

export default function App(){

  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/data')
      .then(response => { console.log(response); return response.json()})
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));

  }, []);
  console.log(data)
  return (
    <div>
      test2
      {data.map(row => (
          <>
          <div>
            {row.responsecode}
            test
          </div>
          <div>{row.responsemessage}</div>
          </>
        ))}
  </div>
  )
};