import {Col, Row, Spinner} from "react-bootstrap";
import DiskCard from '../../components/diskCard/diskCard.jsx';
// import {useState} from 'react';

function MainPage({loading, disks}) {
  return (
    <div className={`container ${loading && 'containerLoading'}`}>
      {loading && <div className="loadingBg"><Spinner animation="border"/></div>}

      <Row xs={4} md={4} className="g-4">
        {disks.map((item, index) => 
          <Col key={index}>
            <DiskCard {...item} />
          </Col>
        )}
      </Row>
    </div>
  );
}

export default MainPage;
