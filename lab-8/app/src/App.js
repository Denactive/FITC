import { BrowserRouter, Route, Routes, Link } from "react-router-dom";
import {useEffect, useState} from 'react';

import MainPage from './pages/main/mainPage.jsx';
import DiskPage from './pages/disk/diskPage.jsx';
// import NewPage from './pages/new/newPage.jsx';
// import StartPage from './pages/start/startPage.jsx';

import urls from './module/urls.js';
import ajax from './module/ajax.js';

function App() {
  const [loading, setLoading] = useState(false);
  const [disks, setDisks] = useState([]);

  const upload = () => {
    setLoading(true);
    ajax.get({url: urls.disks()}).then(({response}) => {
      setDisks(response);
      setLoading(false);
    });
  };

  useEffect(() => {
      // код выполнится на mount`е компонента
      upload();
      return () => {
        // код выполнится на unmount`е компонента
      }
    }, 
  [] // Это список зависимостей хука, он будет вызван каждый раз, когда зависимости будут меняться
  );
  
  return (
    <BrowserRouter basename="/">
      <div>
        {/* <ul>
          <li>
            <Link to="/">Старт</Link>
          </li>
          <li>
            <Link to="/new">Хочу на страницу с чем-то новеньким</Link>
          </li>
        </ul>
        <hr /> */}
        <Routes>
          {/* <Route path="/" element={<StartPage/>}/> */}
          <Route path="/" element={<MainPage loading={loading} disks={disks}/>}/>
          {/* <Route path="/new" element={<NewPage/>}/> */}
          <Route path="/:diskId" element={<DiskPage disks={disks}/>}/>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
