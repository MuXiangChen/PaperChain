from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import List, Literal, Dict, Any
from pathlib import Path
import json


MaterialType = Literal[
    "background",
    "problem_statement",
    "motivation",
    "objective",
    "definition",
    "related_work",
    "method",
    "method_detail",
    "comparison",
    "example",
    "evidence",
    "dataset",
    "metric",
    "result",
    "analysis",
    "discussion",
    "conclusion",
    "future_work",
    "management_implication",
]


ConstraintType = Literal[
    "must_include",
    "min_sentences",
    "max_sentences",
    "min_citations",
    "max_citations",
    "must_use_material_type",
    "forbid_style",
    "require_style",
    "require_keyword",
]


CheckType = Literal[
    "coverage_check",
    "logic_check",
    "citation_check",
    "style_check",
    "structure_check",
    "consistency_check",
]


@dataclass
class HardConstraint:
    """
    硬性规则：必须满足的约束
    """
    constraint_type: ConstraintType
    description: str
    value: Any = None
    required: bool = True


@dataclass
class SelfCheckRule:
    """
    自检规则：生成后需要检查的内容
    """
    check_type: CheckType
    description: str
    criteria: str
    required: bool = True


@dataclass
class WritingGuideline:
    """
    写作规范：包含硬性规则 + 自检规则
    """
    hard_constraints: List[HardConstraint] = field(default_factory=list)
    self_check_rules: List[SelfCheckRule] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    def add_constraint(self, constraint: HardConstraint) -> None:
        self.hard_constraints.append(constraint)

    def add_self_check(self, rule: SelfCheckRule) -> None:
        self.self_check_rules.append(rule)

    def add_note(self, note: str) -> None:
        self.notes.append(note)


@dataclass
class BlueprintPoint:
    """
    写作最小单元
    一个 point 通常对应一句话或一个表达点
    """

    point_id: str
    description: str
    purpose: str

    expected_content: Optional[str] = None

    material_types: List[str] = field(default_factory=list)

    citations_required: bool = False

    rhetorical_style: Optional[str] = None
    # 例如：
    # contrast / enumeration / claim / evidence / summary

    order: int = 0

    metadata: Dict[str, Any] = field(default_factory=dict)

    def short_label(self) -> str:
        citation_text = "需引用" if self.citations_required else "可无引用"
        material_text = ", ".join(self.material_types) if self.material_types else "不限"

        return (
            f"[Point] {self.description} "
            f"({citation_text} | 素材类型: {material_text})"
        )

@dataclass
class BlueprintSlot:
    """
    表示一个固定写作槽位：
    即这一章里“这个位置应该写什么”
    """
    slot_id: str
    name: str
    purpose: str
    expected_content: str
    material_types: List[MaterialType]

    points: List[BlueprintPoint] = field(default_factory=list)

    required: bool = True
    citations_required: bool = False
    min_items: int = 1
    max_items: int = 5
    paragraph_hint: str = "independent_paragraph"
    order: int = 0

    guideline: WritingGuideline = field(default_factory=WritingGuideline)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def short_label(self) -> str:
        required_text = "必填" if self.required else "可选"
        citation_text = "需引用" if self.citations_required else "可无引用"
        material_text = ", ".join(self.material_types)
        return (
            f"[Slot] {self.name} "
            f"({required_text} | {citation_text} | "
            f"素材类型: {material_text})"
        )


@dataclass
class BlueprintSection:
    """
    表示一个章节，可包含：
    - 槽位 slots
    - 子章节 subsections
    """
    section_id: str
    title: str
    purpose: str

    level: int = 1
    description: str = ""
    required: bool = True
    order: int = 0

    slots: List[BlueprintSlot] = field(default_factory=list)
    subsections: List["BlueprintSection"] = field(default_factory=list)

    guideline: WritingGuideline = field(default_factory=WritingGuideline)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_slot(self, slot: BlueprintSlot) -> None:
        self.slots.append(slot)
        self.slots.sort(key=lambda x: x.order)

    def add_subsection(self, subsection: "BlueprintSection") -> None:
        self.subsections.append(subsection)
        self.subsections.sort(key=lambda x: x.order)

    def short_label(self) -> str:
        required_text = "必需章节" if self.required else "可选章节"
        return f"[Section {self.section_id}] {self.title} ({required_text})"
    
@dataclass
class Blueprint:
    """
    表示整篇论文的强约束写作蓝图
    """
    blueprint_id: str
    name: str
    paper_type: str
    discipline: str
    source: str

    description: str = ""
    sections: List[BlueprintSection] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_section(self, section: BlueprintSection) -> None:
        self.sections.append(section)
        self.sections.sort(key=lambda x: x.order)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class TreePrinter:

    def print_blueprint(self, blueprint):
        print(f"\nBlueprint: {blueprint.name}")
        print("=" * 60)

        for section in sorted(blueprint.sections, key=lambda x: x.order):
            self._print_section(section, indent=1)

    def _print_section(self, section, indent):
        prefix = "  " * indent
        print(f"{prefix}📂 Section {section.section_id}: {section.title}")

        # slots
        for slot in sorted(section.slots, key=lambda x: x.order):
            self._print_slot(slot, indent + 1)

        # subsections
        for sub in sorted(section.subsections, key=lambda x: x.order):
            self._print_section(sub, indent + 1)

    def _print_slot(self, slot, indent):
        prefix = "  " * indent

        citation_flag = "📚" if slot.citations_required else ""
        required_flag = "✓" if slot.required else "?"

        print(f"{prefix}🧩 Slot {slot.slot_id}: {slot.name} {required_flag}{citation_flag}")

        # points
        for point in sorted(getattr(slot, "points", []), key=lambda x: x.order):
            self._print_point(point, indent + 1)

    def _print_point(self, point, indent):
        prefix = "  " * indent

        citation_flag = "📚" if point.citations_required else ""

        print(
            f"{prefix}🔹 Point {point.point_id}: {point.description} {citation_flag}"
        )

import json
from pathlib import Path
from typing import Any, Dict, Union


class BlueprintCompiler:
    """
    BlueprintCompiler 负责 Blueprint 与 JSON / dict 之间的双向转换：

    1. 从 BlueprintSpec(dict) 构建 Blueprint
    2. 从本地 JSON 文件加载 Blueprint
    3. 将 Blueprint 导出为 dict
    4. 将 Blueprint 保存为本地 JSON 文件
    """

    def from_dict(self, spec: Dict[str, Any]) -> Blueprint:
        """
        从 BlueprintSpec(dict) 构建 Blueprint 对象
        """
        blueprint = Blueprint(
            blueprint_id=spec["blueprint_id"],
            name=spec["name"],
            paper_type=spec["paper_type"],
            discipline=spec["discipline"],
            source=spec.get("source", "unknown"),
            description=spec.get("description", ""),
        )

        for section_spec in spec.get("sections", []):
            section = self._build_section(section_spec)
            blueprint.add_section(section)

        return blueprint

    def from_json_file(self, file_path: Union[str, Path], encoding: str = "utf-8") -> Blueprint:
        """
        从本地 JSON 文件加载 Blueprint 对象
        """
        file_path = Path(file_path)

        with file_path.open("r", encoding=encoding) as f:
            spec = json.load(f)

        return self.from_dict(spec)

    def to_dict(self, blueprint: Blueprint) -> Dict[str, Any]:
        """
        将 Blueprint 对象导出为 dict
        """
        return {
            "blueprint_id": blueprint.blueprint_id,
            "name": blueprint.name,
            "paper_type": blueprint.paper_type,
            "discipline": blueprint.discipline,
            "source": blueprint.source,
            "description": blueprint.description,
            "sections": [self._section_to_dict(section) for section in blueprint.sections],
        }

    def to_json_file(
        self,
        blueprint: Blueprint,
        file_path: Union[str, Path],
        encoding: str = "utf-8",
        ensure_ascii: bool = False,
        indent: int = 2,
    ) -> None:
        """
        将 Blueprint 对象保存为本地 JSON 文件
        """
        file_path = Path(file_path)
        data = self.to_dict(blueprint)

        with file_path.open("w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=ensure_ascii, indent=indent)

    # -------------------------
    # 内部：dict -> dataclass
    # -------------------------

    def _build_section(self, section_spec: Dict[str, Any]) -> BlueprintSection:
        section = BlueprintSection(
            section_id=section_spec["section_id"],
            title=section_spec["title"],
            purpose=section_spec["purpose"],
            level=section_spec.get("level", 1),
            description=section_spec.get("description", ""),
            required=section_spec.get("required", True),
            order=section_spec.get("order", 0),
        )

        for slot_spec in section_spec.get("slots", []):
            slot = self._build_slot(slot_spec)
            section.add_slot(slot)

        for sub_spec in section_spec.get("subsections", []):
            subsection = self._build_section(sub_spec)
            section.add_subsection(subsection)

        return section

    def _build_slot(self, slot_spec: Dict[str, Any]) -> BlueprintSlot:
        slot = BlueprintSlot(
            slot_id=slot_spec["slot_id"],
            name=slot_spec["name"],
            purpose=slot_spec["purpose"],
            expected_content=slot_spec["expected_content"],
            material_types=slot_spec.get("material_types", []),
            required=slot_spec.get("required", True),
            citations_required=slot_spec.get("citations_required", False),
            min_items=slot_spec.get("min_items", 1),
            max_items=slot_spec.get("max_items", 5),
            paragraph_hint=slot_spec.get("paragraph_hint", "independent_paragraph"),
            order=slot_spec.get("order", 0),
            points=[self._build_point(p) for p in slot_spec.get("points", [])],
            metadata=slot_spec.get("metadata", {}),
        )
        return slot

    def _build_point(self, point_spec: Dict[str, Any]) -> BlueprintPoint:
        return BlueprintPoint(
            point_id=point_spec["point_id"],
            description=point_spec["description"],
            purpose=point_spec["purpose"],
            expected_content=point_spec.get("expected_content"),
            material_types=point_spec.get("material_types", []),
            citations_required=point_spec.get("citations_required", False),
            rhetorical_style=point_spec.get("rhetorical_style"),
            order=point_spec.get("order", 0),
            metadata=point_spec.get("metadata", {}),
        )

    # -------------------------
    # 内部：dataclass -> dict
    # -------------------------

    def _section_to_dict(self, section: BlueprintSection) -> Dict[str, Any]:
        return {
            "section_id": section.section_id,
            "title": section.title,
            "purpose": section.purpose,
            "level": section.level,
            "description": section.description,
            "required": section.required,
            "order": section.order,
            "slots": [self._slot_to_dict(slot) for slot in section.slots],
            "subsections": [self._section_to_dict(sub) for sub in section.subsections],
        }

    def _slot_to_dict(self, slot: BlueprintSlot) -> Dict[str, Any]:
        return {
            "slot_id": slot.slot_id,
            "name": slot.name,
            "purpose": slot.purpose,
            "expected_content": slot.expected_content,
            "material_types": slot.material_types,
            "points": [self._point_to_dict(point) for point in slot.points],
            "required": slot.required,
            "citations_required": slot.citations_required,
            "min_items": slot.min_items,
            "max_items": slot.max_items,
            "paragraph_hint": slot.paragraph_hint,
            "order": slot.order,
            "metadata": slot.metadata,
        }

    def _point_to_dict(self, point: BlueprintPoint) -> Dict[str, Any]:
        return {
            "point_id": point.point_id,
            "description": point.description,
            "purpose": point.purpose,
            "expected_content": point.expected_content,
            "material_types": point.material_types,
            "citations_required": point.citations_required,
            "rhetorical_style": point.rhetorical_style,
            "order": point.order,
            "metadata": point.metadata,
        }

class BlueprintBuilder:
    def load_json(self, filepath: str | Path) -> Dict[str, Any]:
        filepath = Path(filepath)
        with filepath.open("r", encoding="utf-8") as f:
            return json.load(f)

    def build_from_files(
        self,
        ss_file: str | Path,
        ca_file: Optional[str | Path] = None,
    ) -> Blueprint:
        ss_spec = self.load_json(ss_file)
        ca_spec = self.load_json(ca_file) if ca_file else None
        return self.build(ss_spec, ca_spec)

    def build(
        self,
        ss_spec: Dict[str, Any],
        ca_spec: Optional[Dict[str, Any]] = None,
    ) -> Blueprint:
        blueprint = self._compile_base_blueprint(ss_spec)

        if ca_spec:
            self._apply_ca_overrides(blueprint, ca_spec)

        return blueprint

    def _compile_base_blueprint(self, spec: Dict[str, Any]) -> Blueprint:
        blueprint = Blueprint(
            blueprint_id=spec["blueprint_id"],
            name=spec["name"],
            paper_type=spec["paper_type"],
            discipline=spec["discipline"],
            source=spec.get("source", "Standards System"),
            description=spec.get("description", ""),
        )

        for section_spec in spec.get("sections", []):
            section = self._build_section(section_spec)
            blueprint.add_section(section)

        return blueprint

    def _build_section(self, section_spec: Dict[str, Any]) -> BlueprintSection:
        section = BlueprintSection(
            section_id=section_spec["section_id"],
            title=section_spec["title"],
            purpose=section_spec["purpose"],
            level=section_spec.get("level", 1),
            description=section_spec.get("description", ""),
            required=section_spec.get("required", True),
            order=section_spec.get("order", 0),
        )

        for slot_spec in section_spec.get("slots", []):
            slot = self._build_slot(slot_spec)
            section.add_slot(slot)

        for sub_spec in section_spec.get("subsections", []):
            subsection = self._build_section(sub_spec)
            section.add_subsection(subsection)

        return section

    def _build_slot(self, slot_spec: Dict[str, Any]) -> BlueprintSlot:

        points = [
            self._build_point(p) for p in slot_spec.get("points", [])
        ]

        return BlueprintSlot(
            slot_id=slot_spec["slot_id"],
            name=slot_spec["name"],
            purpose=slot_spec["purpose"],
            expected_content=slot_spec["expected_content"],
            material_types=slot_spec.get("material_types", []),

            required=slot_spec.get("required", True),
            citations_required=slot_spec.get("citations_required", False),
            min_items=slot_spec.get("min_items", 1),
            max_items=slot_spec.get("max_items", 5),
            paragraph_hint=slot_spec.get("paragraph_hint", "independent_paragraph"),
            order=slot_spec.get("order", 0),

            points=points,   # ← 关键新增
        )
    
    def _build_point(self, point_spec: Dict[str, Any]) -> BlueprintPoint:

        return BlueprintPoint(
            point_id=point_spec["point_id"],
            description=point_spec["description"],
            purpose=point_spec.get("purpose", ""),
            expected_content=point_spec.get("expected_content"),
            material_types=point_spec.get("material_types", []),
            citations_required=point_spec.get("citations_required", False),
            rhetorical_style=point_spec.get("rhetorical_style"),
            order=point_spec.get("order", 0),
            metadata=point_spec.get("metadata", {}),
        )

    def _apply_ca_overrides(self, blueprint: Blueprint, ca_spec: Dict[str, Any]) -> None:
        for section_override in ca_spec.get("section_overrides", []):
            section = self._find_section(blueprint, section_override["section_id"])
            if not section:
                continue

            if "title" in section_override:
                section.title = section_override["title"]
            if "purpose" in section_override:
                section.purpose = section_override["purpose"]
            if "description" in section_override:
                section.description = section_override["description"]

            guideline_spec = section_override.get("guideline")
            if guideline_spec:
                self._merge_guideline(section.guideline, guideline_spec)

        for slot_override in ca_spec.get("slot_overrides", []):
            slot = self._find_slot(blueprint, slot_override["slot_id"])
            if not slot:
                continue

            if "name" in slot_override:
                slot.name = slot_override["name"]
            if "purpose" in slot_override:
                slot.purpose = slot_override["purpose"]
            if "expected_content" in slot_override:
                slot.expected_content = slot_override["expected_content"]
            if "material_types" in slot_override:
                slot.material_types = slot_override["material_types"]
            if "citations_required" in slot_override:
                slot.citations_required = slot_override["citations_required"]
            if "required" in slot_override:
                slot.required = slot_override["required"]

            guideline_spec = slot_override.get("guideline")
            if guideline_spec:
                self._merge_guideline(slot.guideline, guideline_spec)

    def _merge_guideline(self, guideline: WritingGuideline, spec: Dict[str, Any]) -> None:
        for note in spec.get("notes", []):
            guideline.add_note(note)

        for c in spec.get("hard_constraints", []):
            guideline.add_constraint(HardConstraint(
                constraint_type=c["constraint_type"],
                description=c["description"],
                value=c.get("value"),
                required=c.get("required", True),
            ))

        for r in spec.get("self_check_rules", []):
            guideline.add_self_check(SelfCheckRule(
                check_type=r["check_type"],
                description=r["description"],
                criteria=r["criteria"],
                required=r.get("required", True),
            ))

    def _find_section(self, blueprint: Blueprint, section_id: str) -> Optional[BlueprintSection]:
        def walk(sections):
            for section in sections:
                if section.section_id == section_id:
                    return section
                found = walk(section.subsections)
                if found:
                    return found
            return None

        return walk(blueprint.sections)

    def _find_slot(self, blueprint: Blueprint, slot_id: str) -> Optional[BlueprintSlot]:
        def walk(sections):
            for section in sections:
                for slot in section.slots:
                    if slot.slot_id == slot_id:
                        return slot
                found = walk(section.subsections)
                if found:
                    return found
            return None

        return walk(blueprint.sections)
    
    from typing import Optional, List

