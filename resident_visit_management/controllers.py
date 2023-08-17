from flask import Flask, request, jsonify
from models import Resident, Visitor, Visit, Security
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///resident_visit_management.db')
session = Session(bind=engine)

@app.route('/schedule_visit', methods=['POST'])
def schedule_visit():
    data = request.get_json()
    resident = session.query(Resident).get(data['resident_id'])
    visitor = Visitor(id=data['visitor_id'], name=data['visitor_name'], phone_number=data['visitor_phone_number'], nic=data['visitor_nic'], vehicle_number=data['visitor_vehicle_number'])
    visit = Visit(id=data['visit_id'], scheduled_time=data['scheduled_time'], is_approved=False, resident=resident, visitor=visitor)
    session.add(visitor)
    session.add(visit)
    session.commit()
    return jsonify({'message': 'Visit scheduled successfully'}), 200

@app.route('/approve_visit', methods=['PUT'])
def approve_visit():
    data = request.get_json()
    visit = session.query(Visit).get(data['visit_id'])
    visit.is_approved = True
    session.commit()
    return jsonify({'message': 'Visit approved successfully'}), 200

@app.route('/search_visit', methods=['GET'])
def search_visit():
    visitor_name = request.args.get('visitor')
    visits = session.query(Visit).join(Visitor).filter(Visitor.name == visitor_name).all()
    return jsonify([{'id': visit.id, 'scheduled_time': visit.scheduled_time, 'is_approved': visit.is_approved, 'resident': visit.resident.name, 'visitor': visit.visitor.name} for visit in visits]), 200

@app.route('/create_visit', methods=['POST'])
def create_visit():
    data = request.get_json()
    security = session.query(Security).get(data['security_id'])
    resident = session.query(Resident).get(data['resident_id'])
    visitor = session.query(Visitor).get(data['visitor_id'])
    visit = Visit(id=data['visit_id'], scheduled_time=data['scheduled_time'], is_approved=True, resident=resident, visitor=visitor)
    session.add(visit)
    session.commit()
    return jsonify({'message': 'Visit created successfully'}), 200
