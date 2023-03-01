# Copyright (c) 2023, Pradip and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProcessDefinition(Document):
   
	@frappe.whitelist()
	def qtyupdate(self):
		# temp=''
  
		mqty=0.0
		fpq=0.0
		scq=0.0
		tocq=0.0
		mam=0.0
		fpam=0.0
		scam=0.0
		tbam=0.0
		
		for m in self.get('materials'):
			# temp=m.quantity
			# m.quantity=self.quantity
			mqty=float(mqty)+float(m.quantity)
			tbam=float(m.quantity)*float(m.rate)
			m.amount=tbam
			mam=float(mam)+float(m.amount)
			
		self.materials_qty=mqty
		self.materials_amount=mam
   
		for fp in self.get('finished_products'):
			# fp.quantity=str((int(fp.quantity)*int(self.quantity))/int(temp))
			fpq=float(fpq)+float(fp.quantity)
			tbam=float(fp.quantity)*float(fp.rate)
			fp.amount=tbam
			fpam=float(fpam)+float(fp.amount)
		
		self.finished_products_qty=fpq	
		self.finished_products_amount=fpam
		
		for sc in self.get('scrap'):	
			# sc.quantity=str((int(sc.quantity)*int(self.quantity))/int(temp))
			scq=float(scq)+float(sc.quantity)
			tbam=float(sc.quantity)*float(sc.rate)
			sc.amount=tbam
			scam=float(scam)+float(sc.amount)
		
		self.scrap_qty=scq
		self.scrap_amount=scam
  
		self.all_finish_qty=self.finished_products_qty+self.scrap_qty
		self.total_all_amount=self.finished_products_amount+self.scrap_amount
		
		for toc in self.get('operation_cost'):
			# toc.cost=str((int(toc.cost)*int(self.quantity))/int(temp))
			tocq=float(tocq)+float(toc.cost)
		
		self.total_operation_cost=tocq
