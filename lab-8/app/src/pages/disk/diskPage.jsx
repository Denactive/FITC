import diskDefaultImg from '../../static/img/disk-icon.png';
import {Card, Button} from "react-bootstrap";
import {useParams} from "react-router-dom";

const DiskPage = ({disks}) => {
  const {diskId} = useParams();
  console.log({diskId} , typeof diskId);
  const disk = disks.find((el) => el.id + '' === diskId);
  if (!disk) {
    return null;
  }
  return <div>
    <Button href='/'>Назад</Button>
    <Card className="card" style={{width: '200px'}}>
      <Card.Img className="card-img-top" src={diskDefaultImg} alt={disk.title}/>
      <Card.Body>
        <div className="textStyle">
          <Card.Title>{disk.title}</Card.Title>
        </div>
        <div  className="textStyle">
          <Card.Text>
            {disk.description}
          </Card.Text>
        </div>
      </Card.Body>
    </Card>;
  </div>
}
export default DiskPage;