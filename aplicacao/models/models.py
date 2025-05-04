from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from aplicacao.config.database import Base


class Departamento(Base):
    __tablename__ = 'departamentos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sala = Column(String, index=True)
    bloco = Column(String, index=True)
    telefone = Column(String, index=True)

    equipamentos = relationship('Equipamento', back_populates='departamentos')


class Equipamento(Base):
    __tablename__ = 'equipamentos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    garantia = Column(Boolean)
    ip = Column(String, index=True)
    tipo = Column(String, index=True)

    departamento_id = Column(Integer, ForeignKey('departamentos.id'))
    departamentos = relationship('Departamento', back_populates='equipamentos')

    insumos = relationship('Insumo', back_populates='equipamentos')


class Insumo(Base):
    __tablename__ = 'insumos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, index=True)
    tipo = Column(String, index=True)

    equipamento_id = Column(Integer, ForeignKey('equipamentos.id'), nullable=True)
    equipamentos = relationship('Equipamento', back_populates='insumos')


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    senha = Column(String)
    tipo = Column(String)