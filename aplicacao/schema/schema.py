from typing import List
from pydantic import BaseModel, ConfigDict


class InsumoBase(BaseModel):
    nome: str
    descricao: str | None = None
    tipo: str
    equipamento_id: int


class InsumoCreate(InsumoBase):
    pass


class InsumoUpdate(InsumoBase):
    pass


class Insumo(InsumoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class EquipamentoBase(BaseModel):
    nome: str
    descricao: str | None = None
    garantia: bool | None = None
    ip: str | None
    departamento_id: int


class EquipamentoCreate(EquipamentoBase):
    pass


class EquipamentoUpdate(EquipamentoBase):
    pass


class Equipamento(EquipamentoBase):
    id: int
    insumos: List[Insumo] = []
    model_config = ConfigDict(from_attributes=True)


class DepartamentoBase(BaseModel):
    nome: str
    sala: str | None = None
    bloco: str | None = None
    telefone: str | None = None


class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    pass


class Departamento(DepartamentoBase):
    id: int
    equipamentos: List[Equipamento]  = []
    model_config = ConfigDict(from_attributes=True)
