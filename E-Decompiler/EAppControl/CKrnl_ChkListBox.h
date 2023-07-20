#pragma once
#include "EAppControl.h"

//选择列表框

struct CKrnl_ChkListBox :public EAppControl
{
public:
	CKrnl_ChkListBox();
	static CKrnl_ChkListBox* create();
public:
	std::string GetEventName(int eventIndex)override;
	bool InitControlExtraData(unsigned int propertyAddr, unsigned int propertySize) override;
	std::string GetPropertyName(unsigned int propertyIndex) override;
};